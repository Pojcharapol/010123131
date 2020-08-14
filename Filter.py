class check_bracket:
    def __init__(self):
        self.stack = []

    def check_last(self, test):
        # put method before for loop in create tree class
        for i in range(len(test)):
            if(test[i] == "("):
                # stack index 0 is "(" and stack index 1 is index where "(" exist
                self.stack.append([test[i], i])

            elif(test[i] == ")"):
                position_ = self.stack.pop()
                range_bracket = i - position_[1]
                if(range_bracket == len(test)-1):
                    return test[1:-1]
        
        return test