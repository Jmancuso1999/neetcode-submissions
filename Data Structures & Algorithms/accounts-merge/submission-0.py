class UnionFind:
    def __init__(self, n):
        self.components = n
        self.parents = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        if node != self.parents[node]:
            self.parents[node] = self.find(self.parents[node])
        
        return self.parents[node]
    
    def union(self, u, v):
        nodeU = self.find(u)
        nodeV = self.find(v)

        if nodeU == nodeV:
            return
        
        if self.rank[nodeU] < self.rank[nodeV]:
            self.parents[nodeU] = nodeV
            self.rank[nodeV] += self.rank[nodeU]
        else:
            self.parents[nodeV] = nodeU
            self.rank[nodeU] += self.rank[nodeV]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        emailToAccounts = {} # email, index of account

        # Maps all common emails share to one parent account
        for index, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAccounts:
                    uf.union(emailToAccounts[email], index) # Prev copy of email and new copy
                else:
                    emailToAccounts[email] = index
        
        emailGroups = collections.defaultdict(list) # index: [list of emails]

        # For the given email / index we need to find the lead account (index) of that parent
        # and append that to a specific group
        for email, index in emailToAccounts.items():
            leadAccount = uf.find(index)
            emailGroups[leadAccount].append(email)
        
        result = []
        for index, emails in emailGroups.items():
            result.append([accounts[index][0]] + sorted(emailGroups[index]))
        
        return result

"""
[name, email1, email2,...]

Would Union Find work Here? Goal is to find the same parents in an undirected graph 

 accounts = [
                A                   B
    ["neet","neet@gmail.com","neet_dsa@gmail.com"],
                C
    ["alice","alice@gmail.com"],
                D               E
    ["neet","bob@gmail.com","neet@gmail.com"],
                F
    ["neet","neetcode@gmail.com"]
]

{
    neet@gmail.com: 0, 
    neet_dsa@gmail.com: 0, 
    alice@gmail.com: 1, 
    bob@gmail.com: 2, 
    neetcode@gmail.com: 3
}

Parents - [0, 1, 0, 3]
Rank - [2, 1, 1, 1]

"""