# Learning About Postman Testing

Postman is a powerful tool used for testing APIs. It allows users to send HTTP requests, inspect responses, automate test workflows, and document APIs efficiently.

## Key Concepts

- **Requests:** The core unit in Postman, allowing you to specify an endpoint (URL), HTTP method (GET, POST, etc.), headers, parameters, and body.
- **Collections:** Groups of requests organized for easy reuse and testing.
- **Environments:** Variables stored by environment (e.g., dev, staging) to reuse data in requests.
- **Tests:** Automated scripts (in JavaScript) run after a request to verify correctness of API responses.
- **Pre-request Scripts:** JavaScript code that runs before a request is sent, useful for setting up variables or modifying requests dynamically.
- **Assertions:** Statements within tests that validate response status, body, headers, and content.

## Writing Tests in Postman

- Tests go in the **Tests** tab of a request.
- Use JavaScript and Postman’s `pm` API.

### Common Test Examples

```javascript
// Status code is 200
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

// Response body contains a property
pm.test("Body has username", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property("username");
});

// Response time is less than 500ms
pm.test("Response time is < 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});
```

## Useful Tips

- Use Chai assertion syntax for readable tests.
- Leverage environment variables to make tests reusable.
- Use `pm.environment.set()` and `pm.environment.get()` for dynamic data between requests.

## Resources

- [Postman Learning Center – Writing Tests](https://learning.postman.com/docs/writing-scripts/test-scripts/)
- [Postman Cheat Sheet](https://www.guru99.com/postman-tutorial.html)

---

Feel free to integrate these practices and examples into your API documentation, Postman collections, or project README files for effective Postman-based API testing!