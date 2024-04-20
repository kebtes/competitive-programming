# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class Linked_List_Node:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

"""
LINKED LIST IMPLEMENTATION
class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Linked_List_Node(homepage)

    def visit(self, url: str) -> None:
        self.current.next = Linked_List_Node(url, prev = self.current)
        self.current = self.current.next

        return self.current.val

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.prev:
                self.current = self.current.prev
            else:
                break
        
        return self.current.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.next:
                self.current = self.current.next
            else:
                break

        return self.current.val"""
        

# ARRAY LIST IMPLEMENTATION
class BrowserHistory:
    def __init__(self, homepage: str):
        self.pages = [homepage]
        self.current_page = 0
        self.total_pages = 0

    def visit(self, url: str) -> None:
        self.pages = self.pages[:self.current_page + 1]
        self.pages.append(url)
        self.total_pages = self.current_page + 1
        self.current_page = self.total_pages

    def back(self, steps: int) -> str:
        self.current_page = max(self.current_page - steps, 0)
        return self.pages[self.current_page]

    def forward(self, steps: int) -> str:
        self.current_page = min(self.current_page + steps, self.total_pages)
        return self.pages[self.current_page]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)