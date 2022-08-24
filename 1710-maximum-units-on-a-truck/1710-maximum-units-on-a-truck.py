#sort decending order and use greedy to find the maximum at each step.
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:  
        boxTypes.sort(key=lambda x:-x[1])
        max_units=0
        for box, units in boxTypes:
            if box<=truckSize:
                max_units+=box*units
            else:
                max_units+=truckSize*units
                #at this point we need to use return to end this program
                return max_units
            truckSize-=box
        return max_units    
                
            