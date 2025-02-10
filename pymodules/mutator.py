#!/usr/bin/env python
# encoding: utf-8
"""
Example Python Module for AFLFuzz

@author:     Christian Holler (:decoder)

@license:

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

@contact:    choller@mozilla.com
"""

import re
import config
from call_function_with_timeout import SetTimeoutDecorator
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream
from antlr4.TokenStreamRewriter import TokenStreamRewriter
from antlr4.error.ErrorListener import ConsoleErrorListener
from JavaScriptLexer import JavaScriptLexer as JSL
from JavaScriptParser import JavaScriptParser as JSP
from JavaScriptParserVisitor import JavaScriptParserVisitor as JSV
from JavaScriptParserVisitor2 import JavaScriptParserVisitor2 as JSV2
import tools,shutil,os

@SetTimeoutDecorator(timeout=10)
def checkParsetime(buf0):
    js_sample0 = buf0.decode()
    input_stream0 = InputStream(js_sample0)
    lexer0 = JSL(input_stream0)
    stream0 = CommonTokenStream(lexer0)
    parser0 = JSP(stream0)
    parser0.removeErrorListeners()
    parser0.addErrorListener(ConsoleErrorListener())
    tree0 = parser0.program()
    return True


def parse(buf, add_buf, cur_id, queued_discovered):
    print('============================', cur_id, '============================')
    is_done, is_timeout, erro_message, results = checkParsetime(buf)
    
    if is_timeout == False:
        # 1. clear
        config.ids = []
        config.intervals = {}
        for type in range(0, 200):
            config.intervals[type] = []
        config.texts = {}
        for type in range(0, 200):
            config.texts[type] = []
        config.new_samples = []

        # 2. parse sample1
        js_sample1 = buf.decode()
        input_stream1 = InputStream(js_sample1)
        lexer1 = JSL(input_stream1)
        stream1 = CommonTokenStream(lexer1)
        parser1 = JSP(stream1)
        parser1.removeErrorListeners()
        parser1.addErrorListener(ConsoleErrorListener())
        tree1 = parser1.program()
        if parser1.getNumberOfSyntaxErrors() > 0:
            print("NumberOfSyntaxErrors: " + str(parser1.getNumberOfSyntaxErrors()))
            return 0
        else:
            visitor1 = JSV()
            try:
                visitor1.visit(tree1)
            except RecursionError:
                return

            is_done, is_timeout, erro_message, results = checkParsetime(add_buf)
            if is_timeout == False:
                # 3. parse sample2
                js_sample2 = add_buf.decode()
                input_stream2 = InputStream(js_sample2)
                lexer2 = JSL(input_stream2)
                stream2 = CommonTokenStream(lexer2)
                parser2 = JSP(stream2)
                tree2 = parser2.program()

                visitor2 = JSV2()
                try:
                    visitor2.visit(tree2)
                except RecursionError:
                    pass

            # 4. crossover
            rewriter = TokenStreamRewriter(tokens=stream1)

            for type in range(0, 143):
                for interval in config.intervals[type]:
                    for text in config.texts[type]:
                        # 5. adjust
                        text = " "+text+" "
                        prefix = rewriter.getText("", 0, interval[0])
                        prefix_ids = []
                        for id in config.ids:
                            if id not in prefix_ids:
                                try:
                                    if re.search("[\W]"+id+"[\W]", prefix):
                                        prefix_ids.append(id)
                                except:
                                    pass

                        new_ids = []
                        for id in config.ids:
                            if id not in new_ids and id not in prefix_ids:
                                try:
                                    if re.search("[\W]"+id+"[\W]", text):
                                        new_ids.append(id)
                                except:
                                    pass

                        if len(new_ids) > 0:
                            if len(prefix_ids) > 0:
                                for id in new_ids:
                                    for prefix_id in prefix_ids:
                                        try:
                                            match = list(re.finditer("[\W]"+id+"[\W]", text))
                                            while len(match) > 0:
                                                start = match[0].start()
                                                text = text[0:start+1] + prefix_id + text[start+1+len(id):]
                                                match = list(re.finditer("[\W]"+id+"[\W]", text))
                                        except:
                                            pass

                                        rewriter.replace("", interval[0], interval[1], text.strip())
                                        new_sample = rewriter.getText("", 0, 10000)
                                        rewriter.rollback(rewriter.lastRewriteTokenIndex(""), "")

                                        if new_sample not in config.new_samples:
                                            config.new_samples.append(new_sample)
                                            if len(config.new_samples) > config.sample_size:
                                                return len(config.new_samples)
                        else:
                            rewriter.replace("", interval[0], interval[1], text.strip())
                            new_sample = rewriter.getText("", 0, 10000)
                            rewriter.rollback(rewriter.lastRewriteTokenIndex(""), "")

                            if new_sample not in config.new_samples:
                                config.new_samples.append(new_sample)
                                if len(config.new_samples) > config.sample_size:
                                    return len(config.new_samples)


    return len(config.new_samples)


def fuzz():
    """
    Called per fuzzing iteration.

    @type buf: bytearray
    @param buf: The buffer that should be mutated.

    @type add_buf: bytearray
    @param add_buf: A second buffer that can be used as mutation source.

    @type max_size: int
    @param max_size: Maximum size of the mutated output. The mutation must not
        produce data larger than max_size.

    @rtype: bytearray
    @return: A new bytearray containing the mutated data
    """
    if len(config.new_samples) > 0:
        sample = config.new_samples.pop(0)
    else:
        sample = ""
    return bytearray(sample.encode())


if __name__ == '__main__':
    # js1 = '''
    # function opt(a, b) {
    #     b[0] = 0;
    #     a.length;

    #     for (let i = 0; i < 1; i++)
    #         a[0] = 0;

    #     b[0] = 9.431092e-317;
    # }

    # let arr1 = new Array(1);
    # arr1[0] = 'a';
    # opt(arr1, [0]);

    # let arr2 = [0.1];
    # opt(arr2, arr2);

    # %OptimizeFunctionOnNextCall(opt);

    # opt(arr2, arr2);
    # arr2[0].x;
    # '''
    # js2 = '''
    # class Base {
    #     constructor() {
    #         this.x = 1;
    #     }
    # }
    # class Derived extends Base {
    #     constructor() {
    #         super();
    #     }
    # }
    # let bound = Object.bind();
    # Reflect.construct(Derived, [], bound);
    # %OptimizeFunctionOnNextCall(Derived);
    # new Derived();
    # '''
    # length = parse(js1.encode(), js2.encode())
    # print(length)
    # if length > 0:
    #     for i in range(0, length):
    #     #     with open("/home/b/crossover/custom_mutators/examples/new_samples/"+str(i)+".js", "w") as f:
    #     #         f.write(fuzz().decode())
    #     #         f.close()
    #         print(fuzz().decode())
    #         print("=============================")
    directory = "/home/qbtly/Desktop/PatchFuzz/js/seeds/sm/"
    path = '/home/qbtly/Desktop/aaaaa/c/'
    shutil.rmtree(path)
    os.mkdir(path)
    file5 = tools.select_random_files(directory, num_files=10)
    i = 1
    for file in file5:
        with open(file, 'r') as f:
            js_content = f.read()
            f.close()
        length = parse(js_content.encode(), js_content.encode())
        print("Total Samples: ", length)
        
        if length > 0:
            pathi = os.path.join(path, str(i))
            i += 1
            os.mkdir(pathi)
            for k in range(0, length):
                with open(os.path.join(pathi, str(k) + ".js") , "w") as f:
                    f.write(fuzz().decode())
                    f.close()

# Uncomment and implement the following methods if you want to use a custom
# trimming algorithm. See also the documentation for a better API description.

# def init_trim(buf):
#     '''
#     Called per trimming iteration.
#
#     @type buf: bytearray
#     @param buf: The buffer that should be trimmed.
#
#     @rtype: int
#     @return: The maximum number of trimming steps.
#     '''
#     global ...
#
#     # Initialize global variables
#
#     # Figure out how many trimming steps are possible.
#     # If this is not possible for your trimming, you can
#     # return 1 instead and always return 0 in post_trim
#     # until you are done (then you return 1).
#
#     return steps
#
# def trim():
#     '''
#     Called per trimming iteration.
#
#     @rtype: bytearray
#     @return: A new bytearray containing the trimmed data.
#     '''
#     global ...
#
#     # Implement the actual trimming here
#
#     return bytearray(...)
#
# def post_trim(success):
#     '''
#     Called after each trimming operation.
#
#     @type success: bool5
#     @param success: Indicates if the last trim operation was successful.
#
#     @rtype: int
#     @return: The next trim index (0 to max number of steps) where max
#              number of steps indicates the trimming is done.
#     '''
#     global ...
#
#     if not success:
#         # Restore last known successful input, determine next index
#     else:
#         # Just determine the next index, based on what was successfully
#         # removed in the last step
#
#     return next_index
#
# def post_process(buf):
#     '''
#     Called just before the execution to write the test case in the format
#     expected by the target
#
#     @type buf: bytearray
#     @param buf: The buffer containing the test case to be executed
#
#     @rtype: bytearray
#     @return: The buffer containing the test case after
#     '''
#     return buf
#
# def havoc_mutation(buf, max_size):
#     '''
#     Perform a single custom mutation on a given input.
#
#     @type buf: bytearray
#     @param buf: The buffer that should be mutated.
#
#     @type max_size: int
#     @param max_size: Maximum size of the mutated output. The mutation must not
#         produce data larger than max_size.
#
#     @rtype: bytearray
#     @return: A new bytearray containing the mutated data
#     '''
#     return mutated_buf
#
# def havoc_mutation_probability():
#     '''
#     Called for each `havoc_mutation`. Return the probability (in percentage)
#     that `havoc_mutation` is called in havoc. Be default it is 6%.
#
#     @rtype: int
#     @return: The probability (0-100)
#     '''
#     return prob
#
# def queue_get(filename):
#     '''
#     Called at the beginning of each fuzz iteration to determine whether the
#     test case should be fuzzed
#
#     @type filename: str
#     @param filename: File name of the test case in the current queue entry
#
#     @rtype: bool
#     @return: Return True if the custom mutator decides to fuzz the test case,
#         and False otherwise
#     '''
#     return True
#
# def queue_new_entry(filename_new_queue, filename_orig_queue):
#     '''
#     Called after adding a new test case to the queue
#
#     @type filename_new_queue: str
#     @param filename_new_queue: File name of the new queue entry
#
#     @type filename_orig_queue: str
#     @param filename_orig_queue: File name of the original queue entry
#     '''
#     pass
