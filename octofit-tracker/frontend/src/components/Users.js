import React, { useEffect, useState } from 'react';

// Example Codespace URL: https://$REACT_APP_CODESPACE_NAME-8000.app.github.dev/api/users/

function buildUrl(endpoint) {
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  if (codespace) return `https://${codespace}-8000.app.github.dev/api/${endpoint}/`;
  const proto = window.location.protocol;
  const host = window.location.hostname;
  return `${proto}//${host}:8000/api/${endpoint}/`;
}

function primaryLabel(item) {
  return item.name || item.username || item.email || item.title || item.id || JSON.stringify(item);
}

export default function Users() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);

  const load = () => {
    setLoading(true);
    const url = buildUrl('users');
    console.log('Fetching Users from', url);
    fetch(url)
      .then(res => res.json())
      .then(json => {
        console.log('Users response:', json);
        const items = json.results || json || [];
        setData(items);
      })
      .catch(err => console.error('Users fetch error', err))
      .finally(() => setLoading(false));
  };

  useEffect(() => { load(); }, []);

  return (
    <div className="container mt-3">
      <div className="card">
            <div className="card-header d-flex justify-content-between align-items-center">
          <h5 className="mb-0">Users</h5>
          <div>
            <button aria-label="Refresh Users" className="btn btn-sm btn-primary me-2" onClick={load} disabled={loading}>{loading ? 'Loading...' : 'Refresh'}</button>
            <a aria-label="Open Users API" className="btn btn-sm btn-outline-secondary" href="/api/users/">API Link</a>
          </div>
        </div>
        <div className="card-body">
          <div className="table-responsive">
            <table className="table table-striped">
              <thead>
                <tr>
                  <th>#</th>
                  <th>ID</th>
                  <th>Name</th>
                  <th>Details</th>
                </tr>
              </thead>
              <tbody>
                {data && data.length > 0 ? data.map((item, idx) => (
                  <tr key={item.id || idx}>
                    <td>{idx + 1}</td>
                    <td>{item.id || '-'}</td>
                    <td>{primaryLabel(item)}</td>
                    <td><pre style={{margin:0,whiteSpace:'pre-wrap'}}>{JSON.stringify(item, null, 2)}</pre></td>
                  </tr>
                )) : (
                  <tr>
                    <td colSpan={4} className="text-center">No records found</td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}
