#!/usr/bin/env bash
set -eu

bundle install
bundle exec jekyll serve --incremental
