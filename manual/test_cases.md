## API Test Cases – ReqRes API

### TC_API_001 – GET list of users returns 200
**Endpoint:** `GET https://reqres.in/api/users?page=2`  
**Expected:**  
- Status code = 200  
- Response contains a `data` list  

---

### TC_API_002 – Validate user list structure
**Endpoint:** `GET https://reqres.in/api/users?page=2`  
**Expected:**  
- `data` is an array  
- Each user object contains:  
  - `id`  
  - `email`  
  - `first_name`  
  - `last_name`  
  - `avatar`

---

### TC_API_003 – Invalid endpoint returns 404  
**Endpoint:** `GET https://reqres.in/api/unknown/999`  
**Expected:**  
- Status code = 404

---

### TC_API_004 – Create user returns 201  
**Endpoint:** `POST https://reqres.in/api/users`  
**Body:**  
```json
{
  "name": "morpheus",
  "job": "leader"
}
Expected:

Status code = 201

Response contains:

id

createdAt