class Box:
    def __init__(self, val: str, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Box(homepage)
        self.curr = self.head

    def visit(self, url: str) -> None:
        curr_page = Box(url)
        self.curr.next = curr_page
        curr_page.prev = self.curr
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        n = steps
        while(n > 0 and self.curr.prev):
            self.curr = self.curr.prev
            n -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        n = steps
        while(n > 0 and self.curr.next):
            self.curr = self.curr.next
            n -= 1
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)