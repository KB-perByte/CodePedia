def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item
    
# ff = powerset([1,2,3])
# print(ff)



class py_solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))
    
    def subsetsRecur(self, current, sset):
        print('sset' , sset)
        if sset:
            try:
                print('main', sset[1:])
                print('sub ', current + [sset[0]])
            except:
                print('phata')
                pass
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]

print(py_solution().sub_sets([1,2,3]))
