def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l > 1:
            if k < l:
                nums[:] = nums[l-k:] + nums[:l-k]
            else:
                while k != 0:
                    max_k = l - 1 if k > l - 1 else k
                    nums[:] = nums[l-max_k:] + nums[:l-max_k]
                    k -= max_k