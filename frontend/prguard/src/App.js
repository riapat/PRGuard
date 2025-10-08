import React, { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [prData, setPrData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Placeholder: Fetch PR status and agent insights from backend
    fetch("/api/pr-insights")
      .then((res) => res.json())
      .then((data) => {
        setPrData(data);
        setLoading(false);
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>PRGuard Dashboard</h1>
      </header>
      <main>
        {loading ? (
          <p>Loading PR insights...</p>
        ) : (
          <table>
            <thead>
              <tr>
                <th>PR #</th>
                <th>Status</th>
                <th>Agent Analysis</th>
                <th>Review Metrics</th>
                <th>Merge Allowed</th>
              </tr>
            </thead>
            <tbody>
              {prData.map((pr) => (
                <tr key={pr.id}>
                  <td>{pr.number}</td>
                  <td>{pr.status}</td>
                  <td>{pr.analysis}</td>
                  <td>{pr.review_metrics}</td>
                  <td>{pr.merge_allowed ? "Yes" : "No"}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </main>
    </div>
  );
}

export default App;
