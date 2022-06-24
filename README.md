# how to use

<table>
    <tr>
        <th>Reference</th>
        <th>Method</th>
        <th>Params</th>
        <th>Purpose</th>
    </tr>
    <tr>
        <td>/api</td>
        <td>GET</td>
        <td>None</td>
        <td>Entry point for basic api</td>
    </tr>
    <tr>
        <td>/api/notes/</td>
        <td>GET</td>
        <td>None</td>
        <td>GET all created notes</td>
    </tr>
    <tr>
        <td>/api/notes/{note.id}/</td>
        <td>GET, PUT, PATCH, DELETE, HEAD, OPTIONS</td>
        <td>Note Id</td>
        <td>CRUD for detail note</td>
    </tr>
    <tr>
        <td>/api/notes/create/</td>
        <td>POST, OPTIONS</td>
        <td>None</td>
        <td>Create a note</td>
    </tr>
        <tr>
        <td>/api/notes/delallchosen/</td>
        <td>GET, DELETE, OPTIONS</td>
        <td>None</td>
        <td>GET, Delete all chosen notes</td>
    </tr>
</table>
