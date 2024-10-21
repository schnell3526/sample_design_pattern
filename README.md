# sample_design_pattern
design pattern を学習するためのサンプルリポジトリ

# 実行方法
Dockerimage を利用した実行を想定しています。

各イメージのビルド方法

```bash
bash build.sh
```

## Python

```bash
docker run -it --rm -v $(pwd):/app python-runner <ファイルパス>
```

## Go

実行

```bash
docker run -it --rm -v $(pwd):/app go-runner <ファイルパス>
```

## Rust

実行

```bash
docker run -it --rm -v $(pwd):/app rust-runner <ファイルパス>
```
