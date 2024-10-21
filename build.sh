#!/bin/bash

# スクリプトを中断する関数
abort() {
    echo "エラーが発生しました: $1"
    exit 1
}

# Dockerfileのディレクトリ
DOCKER_DIR=".docker"

# ビルドする言語のリスト
LANGUAGES=("go" "python" "rust")

# 各言語に対してDockerイメージをビルド
for lang in "${LANGUAGES[@]}"; do
    echo "Building ${lang}-runner image..."
    docker build -t "${lang}-runner" -f "${DOCKER_DIR}/Dockerfile_${lang}" . || abort "Failed to build ${lang}-runner"
    echo "${lang}-runner image built successfully."
    echo
done

echo "All images have been built successfully."
