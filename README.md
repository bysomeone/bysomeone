Backend and distributed-systems engineer. I build Go-based blockchain infrastructure — the
layer where a bug can cost real money and a bad block cannot be rolled back.

## Selected work

| Project | What it is | My part |
|---|---|---|
| [chain33](https://github.com/33cn/chain33) | Open-source modular blockchain framework; public mainnet since 2018 | Core maintainer since 2018 — 1,060 commits |
| [plugin](https://github.com/33cn/plugin) | The framework's plugin ecosystem: consensus, dapps, cross-chain, L2 | Core maintainer — 509 commits |

## What I work on

- **P2P networking** — pluggable transport and sub-protocol layers, gossip broadcast with
  deduplication, DHT peer discovery, DoS protection driven by validation feedback
- **Consensus and finality** — Snowman/Avalanche adapter, fork preference, out-of-order block
  acceptance
- **Cross-chain and custody** — three-layer bridge design (TSS threshold custody, on-chain proof
  verification, asset state mapping); BTC and other Bitcoin-native assets
- **Storage, state, and compatibility** — persistent state machines, LevelDB/Badger storage,
  EVM address and precision mapping, Bitcoin Script, M-of-N and CSV (CheckSequenceVerify) account
  templates
- **Performance and reliability** — pprof and GC tuning, end-to-end benchmarking, concurrency and
  consistency debugging

## How I work

I define boundaries, failure modes, and acceptance criteria before implementation, and keep
verification independent of the author. I use AI heavily for implementation, review what ships,
and own the design and the correctness call. Stacks I've shipped in: Go, C/C++, Rust — across
embedded, backend, and blockchain systems.

## Contact

cryplo@foxmail.com · Hangzhou, China
