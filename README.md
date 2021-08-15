# Shazam Chart CLI tool

> This tool requires `python >= 3.6`

### Installation
> Ensure you have python3 installed and available in your `PATH`
```bash
make install
```

### Usage

> Aggregate level
```bash
shazam-charts chart 3
```
```
1    Shape Of You    Ed Sheeran
2    24k Magic        Bruno Mars
3    This girl        Kungs
```

> State level
```bash
shazam-charts state_chart 1
```
```
Maryland
1    Shape Of You    Ed Sheeran
2    24k Magic        Bruno Mars
3    This girl        Kungs

Georgia
1    Shape Of You    Ed Sheeran
2    24k Magic        Bruno Mars
3    This girl        Kungs

...
```

### Tests
```bash
make test
```
