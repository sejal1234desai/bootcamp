# 🔐 Login Flow - Mermaid Diagram
# 🛒 Login + Checkout Flow


```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant Server
    participant DB

    User->>Frontend: Visit /login
    User->>Frontend: Enter email & password
    Frontend->>Frontend: Validate inputs (empty fields, email format)
    Frontend->>Server: POST /api/login with credentials
    Server->>DB: Check email & password hash
    alt Valid credentials
        DB-->>Server: Match found
        Server-->>Frontend: Auth token/session
        Frontend-->>User: Redirect to dashboard
    else Invalid credentials
        DB-->>Server: No match
        Server-->>Frontend: Error message
        Frontend-->>User: Show "Invalid login" message
    end
