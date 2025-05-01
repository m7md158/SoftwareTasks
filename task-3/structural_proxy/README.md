## The Proxy Design Pattern 
 - a structural design pattern is a way to use a placeholder object to control access to another object. Instead of interacting directly with the main object, the client talks to the proxy, which then manages the interaction. This is useful for things like controlling access, delaying object creation until it’s needed (lazy initialization), logging, or adding security checks.


## 🧠 Main Idea: Library System
1. When a book is requested, the system searches for it in the database (which is slow or costly).

2. We use a Proxy with Caching to store books that were accessed recently.

3. If the same book is requested again → it's returned from the cache instead of performing a new search.