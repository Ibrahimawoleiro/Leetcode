class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        #The parent array represents the ultimate parent for each index
        parent = [num for num in range(len(accounts))]

        #The size array represents number of emails that are connected to the the current index
        size = [0 for num in range(len(accounts))]

        #Function to get the ultimate parent
        def find_ultimate_parent(node):
            if node == parent[node]:
                return node

            ultimate_parent =  find_ultimate_parent(parent[node])

            parent[node] = ultimate_parent

            return ultimate_parent
            
        #The dictionary below is used to check 
        #if the email has been seen before.
        #If yes, join the two accounts
        #If not, add the email to the seen emails

        store = {}
        owner = {}
        #Loop through the accounts

        for account_index in range(len(accounts)):
            
            for emails_index in range(1,len(accounts[account_index])):

                if accounts[account_index][emails_index] not in store:
                    if account_index not in owner:
                        owner[account_index] = accounts[account_index][0]
                    store[accounts[account_index][emails_index]] = account_index
                    size[account_index] += 1

                else:

                    curr_parent_of_email = store[accounts[account_index][emails_index]] 

                    curr_index = account_index

                    prev_ul = find_ultimate_parent(curr_parent_of_email)

                    curr_ul = find_ultimate_parent(curr_index)

                    if prev_ul != curr_ul:

                        if size[prev_ul] >= size[curr_ul]:
                            size[prev_ul] += size[curr_ul]
                            parent[curr_ul] = prev_ul
                        else:
                            size[curr_ul] += size[prev_ul]
                            parent[prev_ul] = curr_ul
                
        for index in range(len(parent)):
            ul = find_ultimate_parent(parent[index])
            parent[index] = ul
        
        answer = {}

        for email, location in store.items():
            
            ul = find_ultimate_parent(location)

            if ul not in answer:
                answer[ul] = []
                #answer[ul].append(owner[ul])
                answer[ul].append(email)

            else:
                answer[ul].append(email)
        
        result = []
        for key,val in answer.items():
            answer[key].sort()
        for key in owner:
            if key in answer:
                answer[key].insert(0, owner[key])
                result.append(answer[key])

        return result