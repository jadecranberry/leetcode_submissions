#bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)
#Locate the insertion point for x in a to maintain sorted order. The parameters lo and hi may be used to specify a subset of the list which should be considered
#The returned insertion point i partitions the array a into two halves so that all(val < x for val in a[lo : i]) for the left side and all(val >= x for val in a[i : hi]) for the right side.

class Solution:  
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res, prefix, i = [], '', 0
        for c in searchWord:
            prefix += c
            #find i (the starting spot of returned words)
            i=bisect.bisect_left(products, prefix, i)
            res.append([w for w in products[i:i+3] if w.startswith(prefix)])
        return res    
