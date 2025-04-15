#!/bin/bash

set -x  # 启用命令追踪，实时输出执行过程

# ==== 配置部分 ====
AFL_OUT_DIR="/home/out-superion/jsc/default/"
TARGET="/home/WebKit/cov/JSCOnly/Release/bin/jsc"
SRC_DIR="/home/WebKit/cov/"
COV_TOOL="afl-cov/afl-cov"
LOG_DIR="$AFL_OUT_DIR/cov_reports"

# 创建日志目录
mkdir -p "$LOG_DIR"

# 当前时间戳
TIMESTAMP=$(date +"%Y%m%d_%H%M")

# 生成输出目录
# OUTDIR="$LOG_DIR/coverage_$TIMESTAMP"
# mkdir -p "$OUTDIR"

# 执行覆盖率分析（不使用 --live，每次一次性分析）
python2 "$COV_TOOL" \
  --overwrite \
  --cover-corpus \
  --enable-branch-coverage \
  --disable-gcov-check DISABLE_GCOV_CHECK\
  -d "$AFL_OUT_DIR" \
  --coverage-cmd "timeout -s SIGKILL 1 $TARGET AFL_FILE" \
  --code-dir "$SRC_DIR" 

# echo "[✓] 覆盖率分析完成，结果保存在 $OUTDIR"
echo "[✓] 覆盖率分析完成，结果保存在"
