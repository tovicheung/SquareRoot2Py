# SquareRoot2Py

https://www.youtube.com/watch?v=ktRwfBMV4S8

The `SquareRoot2Py` package aims to remove the hassle of computing the square root of 2.

Features
- computing the square root of 2
- up to 16 decimal places of precision
- cross-platform support
- O(1) algorithm
- clear and concise naming

## Installation

```
pip install SquareRoot2Py
```

## Benchmark

Our state-of-the-art algorithm computes the rounded value of the square root of 2 almost **twice as fast** than the built-in C implementation.

#### Built-in C implementation

```python
>>> timeit("a = round(2 ** 0.5)", number=10000000)
0.46002930000031483
```

#### SquareRoot2Py

```python
>>> timeit("a = SquareRoot2Py.RoundedSquareRoot2Py.compute_rounded_square_root_of_2()", setup="import SquareRoot2Py.RoundedSquareRoot2Py", number=10000000)
0.26070590000017546
```

## Examples

To compute the square root of 2 easily:
```python
import SquareRoot2Py
print(SquareRoot2Py.compute_square_root_of_2())
```

If you would like to round the result:
```python
import SquareRoot2Py.RoundedSquareRoot2Py
print(RoundedSquareRoot2Py.compute_rounded_square_root_of_2())
```

For more complex usecases such as calculating the US Government Budget, adjustable rounding can be used:
```python
import SquareRoot2Py.SquareRoot2PyWithAdjustableRounding
print(SquareRoot2Py.SquareRoot2PyWithAdjustableRounding.compute_square_root_of_2_with_adjustable_rounding(3))
```

We are aware that the name `SquareRoot2Py.SquareRoot2PyWithAdjustableRounding` might be too long
Therefore, the following alias is introduced:
```python
import SquareRoot2Py
print(SquareRoot2Py.WithAdjustableRounding.compute_square_root_of_2_with_adjustable_rounding())
```
