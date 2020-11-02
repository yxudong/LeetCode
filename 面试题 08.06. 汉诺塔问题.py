#Tips: recursive

class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        def move(num, _A, _B, _C):
            if num == 1:
                _C.append(_A[-1])
                _A.pop()
            else:
                # 将 A 上面 n - 1 个通过 C 移到 B
                move(num - 1, _A, _C, _B)
                # 将 A 最后一个移到 C
                _C.append(_A[-1])
                _A.pop()
                # 这时，A 空了
                # 将 B 上面 n - 1 个通过空的 A 移到 C
                move(num - 1, _B, _A, _C)
            return

        move(len(A), A, B, C)
        return
