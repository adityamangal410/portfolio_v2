#!/usr/bin/env bash
set -euo pipefail

version=${QUARTO_VERSION:-1.7.31}
url="https://github.com/quarto-dev/quarto-cli/releases/download/v${version}/quarto-${version}-linux-amd64.tar.gz"

mkdir -p /tmp/quarto
curl -L "$url" -o /tmp/quarto/quarto.tar.gz

# Extract and strip first component
cd /tmp/quarto
tar -xzf quarto.tar.gz --strip-components=1
