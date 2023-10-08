class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        checker = set()
        
        checker1 = set()
        checker2 = set()
        checker3 = set()
        checker4 = set()
        checker5 = set()
        checker6 = set()
        checker7 = set()
        checker8 = set()
        checker9 = set()
        
        for num in list(range(9)):

            for number in list(range(9)):
         
                if board[num][number] in checker and board[num][number] != ".":
                    return False
                else:
                    if(num in range(3)):
                        if(number in range(3)):
                            if board[num][number] in checker1 and board[num][number]!=".":
                                print("liar")
                                return False
                            checker1.add(board[num][number])
                        elif number in range(3,6):
                            if board[num][number] in checker2 and board[num][number]!=".":
                                return False
                            checker2.add(board[num][number])
                        elif number in range(6,9):
                            if board[num][number] in checker3 and board[num][number]!=".":
                                return False
                            checker3.add(board[num][number])
                    elif num in range(3,6):
                        if(number in range(3)):
                            if board[num][number] in checker4 and board[num][number]!=".":
                                return False
                            checker4.add(board[num][number])
                        elif number in range(3,6):
                            if board[num][number] in checker5 and board[num][number]!=".":
                                return False
                            checker5.add(board[num][number])
                        elif number in range(6,9):
                            if board[num][number] in checker6 and board[num][number]!=".":
                                return False
                            checker6.add(board[num][number])
                    elif num in range(6,9):
                        if(number in range(3)):
                            if board[num][number] in checker7 and board[num][number]!=".":
                                return False
                            checker7.add(board[num][number])
                        elif number in range(3,6):
                            if board[num][number] in checker8 and board[num][number]!=".":
                                return False
                            checker8.add(board[num][number])
                        elif number in range(6,9):
                            if board[num][number] in checker9 and board[num][number]!=".":
                                return False
                            checker9.add(board[num][number])
                    checker.add(board[num][number])  
            checker = set()
        print(checker3)
        
        
        for num in list(range(9)):
            for number in list(range(9)):
                
                        
                if board[number][num] in checker and board[number][num]!=".":
                    return False
                else:
                    
                    checker.add(board[number][num]) 
            checker = set()
            
        print(checker8)
            
        
        
        
        return True