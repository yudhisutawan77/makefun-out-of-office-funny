# Funniest One-Line Out-of-Office Reply

[![make.fun](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/yudhisutawan77/makefun-out-of-office-funny/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/yudhisutawan77/makefun-out-of-office-funny/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)

Entry for the [Funniest One-Line Out-of-Office Reply](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8) bounty on [make.fun](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8).

## The reply

> I'm away until Monday; your email will be answered in the order it was ignored.

79 characters, one line. A fresh turn on the standard away message: instead of
promising mail will be answered in the order it arrived, it admits the honest
queueing policy up front. It reads like a real message a person would switch
on before going away, and the laugh lands on the first read.

## How it works

`main.py` writes the reply to `/output/entry.txt` (or to `$ENTRY_OUT` /
`$ENTRY_OUT_DIR` when set) and prints the same text to stdout. It validates
the entry first: UTF-8, 1–160 characters, a single non-blank line — the
bounty's gate.

```sh
python3 main.py
cat /output/entry.txt
```
