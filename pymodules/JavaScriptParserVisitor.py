# Generated from JavaScriptParser.g4 by ANTLR 4.13.1
from antlr4 import *
import config
if "." in __name__:
    from .JavaScriptParser import JavaScriptParser
else:
    from JavaScriptParser import JavaScriptParser

# This class defines a complete generic visitor for a parse tree produced by JavaScriptParser.

class JavaScriptParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JavaScriptParser#program.
    def visitProgram(self, ctx:JavaScriptParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#sourceElement.
    def visitSourceElement(self, ctx:JavaScriptParser.SourceElementContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#statement.
    def visitStatement(self, ctx:JavaScriptParser.StatementContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#block.
    def visitBlock(self, ctx:JavaScriptParser.BlockContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#statementList.
    def visitStatementList(self, ctx:JavaScriptParser.StatementListContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#importStatement.
    def visitImportStatement(self, ctx:JavaScriptParser.ImportStatementContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#importFromBlock.
    def visitImportFromBlock(self, ctx:JavaScriptParser.ImportFromBlockContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#importModuleItems.
    def visitImportModuleItems(self, ctx:JavaScriptParser.ImportModuleItemsContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#importAliasName.
    def visitImportAliasName(self, ctx:JavaScriptParser.ImportAliasNameContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#moduleExportName.
    def visitModuleExportName(self, ctx:JavaScriptParser.ModuleExportNameContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#importedBinding.
    def visitImportedBinding(self, ctx:JavaScriptParser.ImportedBindingContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#importDefault.
    def visitImportDefault(self, ctx:JavaScriptParser.ImportDefaultContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#importNamespace.
    def visitImportNamespace(self, ctx:JavaScriptParser.ImportNamespaceContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#importFrom.
    def visitImportFrom(self, ctx:JavaScriptParser.ImportFromContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#aliasName.
    def visitAliasName(self, ctx:JavaScriptParser.AliasNameContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ExportDeclaration.
    def visitExportDeclaration(self, ctx:JavaScriptParser.ExportDeclarationContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ExportDefaultDeclaration.
    def visitExportDefaultDeclaration(self, ctx:JavaScriptParser.ExportDefaultDeclarationContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#exportFromBlock.
    def visitExportFromBlock(self, ctx:JavaScriptParser.ExportFromBlockContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#exportModuleItems.
    def visitExportModuleItems(self, ctx:JavaScriptParser.ExportModuleItemsContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#exportAliasName.
    def visitExportAliasName(self, ctx:JavaScriptParser.ExportAliasNameContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#declaration.
    def visitDeclaration(self, ctx:JavaScriptParser.DeclarationContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#variableStatement.
    def visitVariableStatement(self, ctx:JavaScriptParser.VariableStatementContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#variableDeclarationList.
    def visitVariableDeclarationList(self, ctx:JavaScriptParser.VariableDeclarationListContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:JavaScriptParser.VariableDeclarationContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#emptyStatement_.
    def visitEmptyStatement_(self, ctx:JavaScriptParser.EmptyStatement_Context):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#expressionStatement.
    def visitExpressionStatement(self, ctx:JavaScriptParser.ExpressionStatementContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ifStatement.
    def visitIfStatement(self, ctx:JavaScriptParser.IfStatementContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#DoStatement.
    def visitDoStatement(self, ctx:JavaScriptParser.DoStatementContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#WhileStatement.
    def visitWhileStatement(self, ctx:JavaScriptParser.WhileStatementContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ForStatement.
    def visitForStatement(self, ctx:JavaScriptParser.ForStatementContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ForInStatement.
    def visitForInStatement(self, ctx:JavaScriptParser.ForInStatementContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ForOfStatement.
    def visitForOfStatement(self, ctx:JavaScriptParser.ForOfStatementContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#varModifier.
    def visitVarModifier(self, ctx:JavaScriptParser.VarModifierContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#continueStatement.
    def visitContinueStatement(self, ctx:JavaScriptParser.ContinueStatementContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#breakStatement.
    def visitBreakStatement(self, ctx:JavaScriptParser.BreakStatementContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#returnStatement.
    def visitReturnStatement(self, ctx:JavaScriptParser.ReturnStatementContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#yieldStatement.
    def visitYieldStatement(self, ctx:JavaScriptParser.YieldStatementContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#withStatement.
    def visitWithStatement(self, ctx:JavaScriptParser.WithStatementContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#switchStatement.
    def visitSwitchStatement(self, ctx:JavaScriptParser.SwitchStatementContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#caseBlock.
    def visitCaseBlock(self, ctx:JavaScriptParser.CaseBlockContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#caseClauses.
    def visitCaseClauses(self, ctx:JavaScriptParser.CaseClausesContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#caseClause.
    def visitCaseClause(self, ctx:JavaScriptParser.CaseClauseContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#defaultClause.
    def visitDefaultClause(self, ctx:JavaScriptParser.DefaultClauseContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#labelledStatement.
    def visitLabelledStatement(self, ctx:JavaScriptParser.LabelledStatementContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#throwStatement.
    def visitThrowStatement(self, ctx:JavaScriptParser.ThrowStatementContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#tryStatement.
    def visitTryStatement(self, ctx:JavaScriptParser.TryStatementContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#catchProduction.
    def visitCatchProduction(self, ctx:JavaScriptParser.CatchProductionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#finallyProduction.
    def visitFinallyProduction(self, ctx:JavaScriptParser.FinallyProductionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#debuggerStatement.
    def visitDebuggerStatement(self, ctx:JavaScriptParser.DebuggerStatementContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:JavaScriptParser.FunctionDeclarationContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#classDeclaration.
    def visitClassDeclaration(self, ctx:JavaScriptParser.ClassDeclarationContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#classTail.
    def visitClassTail(self, ctx:JavaScriptParser.ClassTailContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#classElement.
    def visitClassElement(self, ctx:JavaScriptParser.ClassElementContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#methodDefinition.
    def visitMethodDefinition(self, ctx:JavaScriptParser.MethodDefinitionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#fieldDefinition.
    def visitFieldDefinition(self, ctx:JavaScriptParser.FieldDefinitionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#classElementName.
    def visitClassElementName(self, ctx:JavaScriptParser.ClassElementNameContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#privateIdentifier.
    def visitPrivateIdentifier(self, ctx:JavaScriptParser.PrivateIdentifierContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#formalParameterList.
    def visitFormalParameterList(self, ctx:JavaScriptParser.FormalParameterListContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#formalParameterArg.
    def visitFormalParameterArg(self, ctx:JavaScriptParser.FormalParameterArgContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#lastFormalParameterArg.
    def visitLastFormalParameterArg(self, ctx:JavaScriptParser.LastFormalParameterArgContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#functionBody.
    def visitFunctionBody(self, ctx:JavaScriptParser.FunctionBodyContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#sourceElements.
    def visitSourceElements(self, ctx:JavaScriptParser.SourceElementsContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#arrayLiteral.
    def visitArrayLiteral(self, ctx:JavaScriptParser.ArrayLiteralContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#elementList.
    def visitElementList(self, ctx:JavaScriptParser.ElementListContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#arrayElement.
    def visitArrayElement(self, ctx:JavaScriptParser.ArrayElementContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#PropertyExpressionAssignment.
    def visitPropertyExpressionAssignment(self, ctx:JavaScriptParser.PropertyExpressionAssignmentContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ComputedPropertyExpressionAssignment.
    def visitComputedPropertyExpressionAssignment(self, ctx:JavaScriptParser.ComputedPropertyExpressionAssignmentContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#FunctionProperty.
    def visitFunctionProperty(self, ctx:JavaScriptParser.FunctionPropertyContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#PropertyGetter.
    def visitPropertyGetter(self, ctx:JavaScriptParser.PropertyGetterContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#PropertySetter.
    def visitPropertySetter(self, ctx:JavaScriptParser.PropertySetterContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#PropertyShorthand.
    def visitPropertyShorthand(self, ctx:JavaScriptParser.PropertyShorthandContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#propertyName.
    def visitPropertyName(self, ctx:JavaScriptParser.PropertyNameContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#arguments.
    def visitArguments(self, ctx:JavaScriptParser.ArgumentsContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#argument.
    def visitArgument(self, ctx:JavaScriptParser.ArgumentContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#expressionSequence.
    def visitExpressionSequence(self, ctx:JavaScriptParser.ExpressionSequenceContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#TemplateStringExpression.
    def visitTemplateStringExpression(self, ctx:JavaScriptParser.TemplateStringExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#TernaryExpression.
    def visitTernaryExpression(self, ctx:JavaScriptParser.TernaryExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#LogicalAndExpression.
    def visitLogicalAndExpression(self, ctx:JavaScriptParser.LogicalAndExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#PowerExpression.
    def visitPowerExpression(self, ctx:JavaScriptParser.PowerExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#PreIncrementExpression.
    def visitPreIncrementExpression(self, ctx:JavaScriptParser.PreIncrementExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ObjectLiteralExpression.
    def visitObjectLiteralExpression(self, ctx:JavaScriptParser.ObjectLiteralExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#MetaExpression.
    def visitMetaExpression(self, ctx:JavaScriptParser.MetaExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#InExpression.
    def visitInExpression(self, ctx:JavaScriptParser.InExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#LogicalOrExpression.
    def visitLogicalOrExpression(self, ctx:JavaScriptParser.LogicalOrExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#OptionalChainExpression.
    def visitOptionalChainExpression(self, ctx:JavaScriptParser.OptionalChainExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#NotExpression.
    def visitNotExpression(self, ctx:JavaScriptParser.NotExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#PreDecreaseExpression.
    def visitPreDecreaseExpression(self, ctx:JavaScriptParser.PreDecreaseExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ArgumentsExpression.
    def visitArgumentsExpression(self, ctx:JavaScriptParser.ArgumentsExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#AwaitExpression.
    def visitAwaitExpression(self, ctx:JavaScriptParser.AwaitExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ThisExpression.
    def visitThisExpression(self, ctx:JavaScriptParser.ThisExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#FunctionExpression.
    def visitFunctionExpression(self, ctx:JavaScriptParser.FunctionExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#UnaryMinusExpression.
    def visitUnaryMinusExpression(self, ctx:JavaScriptParser.UnaryMinusExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#AssignmentExpression.
    def visitAssignmentExpression(self, ctx:JavaScriptParser.AssignmentExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#PostDecreaseExpression.
    def visitPostDecreaseExpression(self, ctx:JavaScriptParser.PostDecreaseExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#TypeofExpression.
    def visitTypeofExpression(self, ctx:JavaScriptParser.TypeofExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#InstanceofExpression.
    def visitInstanceofExpression(self, ctx:JavaScriptParser.InstanceofExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#UnaryPlusExpression.
    def visitUnaryPlusExpression(self, ctx:JavaScriptParser.UnaryPlusExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#DeleteExpression.
    def visitDeleteExpression(self, ctx:JavaScriptParser.DeleteExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ImportExpression.
    def visitImportExpression(self, ctx:JavaScriptParser.ImportExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#EqualityExpression.
    def visitEqualityExpression(self, ctx:JavaScriptParser.EqualityExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#BitXOrExpression.
    def visitBitXOrExpression(self, ctx:JavaScriptParser.BitXOrExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#SuperExpression.
    def visitSuperExpression(self, ctx:JavaScriptParser.SuperExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#MultiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:JavaScriptParser.MultiplicativeExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#BitShiftExpression.
    def visitBitShiftExpression(self, ctx:JavaScriptParser.BitShiftExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ParenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:JavaScriptParser.ParenthesizedExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#AdditiveExpression.
    def visitAdditiveExpression(self, ctx:JavaScriptParser.AdditiveExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#RelationalExpression.
    def visitRelationalExpression(self, ctx:JavaScriptParser.RelationalExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#PostIncrementExpression.
    def visitPostIncrementExpression(self, ctx:JavaScriptParser.PostIncrementExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#YieldExpression.
    def visitYieldExpression(self, ctx:JavaScriptParser.YieldExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#BitNotExpression.
    def visitBitNotExpression(self, ctx:JavaScriptParser.BitNotExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#NewExpression.
    def visitNewExpression(self, ctx:JavaScriptParser.NewExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#LiteralExpression.
    def visitLiteralExpression(self, ctx:JavaScriptParser.LiteralExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ArrayLiteralExpression.
    def visitArrayLiteralExpression(self, ctx:JavaScriptParser.ArrayLiteralExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#MemberDotExpression.
    def visitMemberDotExpression(self, ctx:JavaScriptParser.MemberDotExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ClassExpression.
    def visitClassExpression(self, ctx:JavaScriptParser.ClassExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#MemberIndexExpression.
    def visitMemberIndexExpression(self, ctx:JavaScriptParser.MemberIndexExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#IdentifierExpression.
    def visitIdentifierExpression(self, ctx:JavaScriptParser.IdentifierExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
                if text not in config.builtins and text not in config.ids:
                    config.ids.append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#BitAndExpression.
    def visitBitAndExpression(self, ctx:JavaScriptParser.BitAndExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#BitOrExpression.
    def visitBitOrExpression(self, ctx:JavaScriptParser.BitOrExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#AssignmentOperatorExpression.
    def visitAssignmentOperatorExpression(self, ctx:JavaScriptParser.AssignmentOperatorExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#VoidExpression.
    def visitVoidExpression(self, ctx:JavaScriptParser.VoidExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#CoalesceExpression.
    def visitCoalesceExpression(self, ctx:JavaScriptParser.CoalesceExpressionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#initializer.
    def visitInitializer(self, ctx:JavaScriptParser.InitializerContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#assignable.
    def visitAssignable(self, ctx:JavaScriptParser.AssignableContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#objectLiteral.
    def visitObjectLiteral(self, ctx:JavaScriptParser.ObjectLiteralContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#AnonymousFunctionDecl.
    def visitAnonymousFunctionDecl(self, ctx:JavaScriptParser.AnonymousFunctionDeclContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#ArrowFunction.
    def visitArrowFunction(self, ctx:JavaScriptParser.ArrowFunctionContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#arrowFunctionParameters.
    def visitArrowFunctionParameters(self, ctx:JavaScriptParser.ArrowFunctionParametersContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#arrowFunctionBody.
    def visitArrowFunctionBody(self, ctx:JavaScriptParser.ArrowFunctionBodyContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:JavaScriptParser.AssignmentOperatorContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#literal.
    def visitLiteral(self, ctx:JavaScriptParser.LiteralContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#templateStringLiteral.
    def visitTemplateStringLiteral(self, ctx:JavaScriptParser.TemplateStringLiteralContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#templateStringAtom.
    def visitTemplateStringAtom(self, ctx:JavaScriptParser.TemplateStringAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#numericLiteral.
    def visitNumericLiteral(self, ctx:JavaScriptParser.NumericLiteralContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#bigintLiteral.
    def visitBigintLiteral(self, ctx:JavaScriptParser.BigintLiteralContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#getter.
    def visitGetter(self, ctx:JavaScriptParser.GetterContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#setter.
    def visitSetter(self, ctx:JavaScriptParser.SetterContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#identifierName.
    def visitIdentifierName(self, ctx:JavaScriptParser.IdentifierNameContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
                if text not in config.builtins and text not in config.ids:
                    config.ids.append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#identifier.
    def visitIdentifier(self, ctx:JavaScriptParser.IdentifierContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#reservedWord.
    def visitReservedWord(self, ctx:JavaScriptParser.ReservedWordContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#keyword.
    def visitKeyword(self, ctx:JavaScriptParser.KeywordContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#let_.
    def visitLet_(self, ctx:JavaScriptParser.Let_Context):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaScriptParser#eos.
    def visitEos(self, ctx:JavaScriptParser.EosContext):
        if ctx!=None and ctx.start!=None and ctx.stop!=None:
            interval = ctx.getSourceInterval()
            if not ctx.start.start > ctx.stop.stop:
                if interval not in config.intervals[ctx.getRuleIndex()]:
                    config.intervals[ctx.getRuleIndex()].append(interval)
                text = ctx.start.getTokenSource().inputStream.getText(ctx.start.start, ctx.stop.stop)
                if ctx.stop.stop-ctx.start.start<config.token_size and text not in config.texts[ctx.getRuleIndex()]:
                    config.texts[ctx.getRuleIndex()].append(text)
        return self.visitChildren(ctx)



del JavaScriptParser