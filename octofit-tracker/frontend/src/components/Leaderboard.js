import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

  useEffect(() => {
    console.log('Leaderboard component - Fetching from:', apiUrl);
    
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Leaderboard component - Raw data received:', data);
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        console.log('Leaderboard component - Processed data:', leaderboardData);
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Leaderboard component - Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, [apiUrl]);

  if (loading) {
    return (
      <div className="container mt-4">
        <div className="loading-spinner">
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
        </div>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="container mt-4">
        <div className="alert alert-danger" role="alert">
          <h4 className="alert-heading">Error!</h4>
          <p className="mb-0">{error}</p>
        </div>
      </div>
    );
  }

  const getRankBadge = (rank) => {
    if (rank === 1) return <span className="badge bg-warning text-dark">🥇 1st</span>;
    if (rank === 2) return <span className="badge bg-secondary">🥈 2nd</span>;
    if (rank === 3) return <span className="badge bg-danger">🥉 3rd</span>;
    return <span className="badge bg-light text-dark">{rank}th</span>;
  };

  return (
    <div className="container mt-4">
      <div className="page-header text-center">
        <h2>Leaderboard</h2>
        <p className="mb-0 mt-2">Compete and see how you rank</p>
      </div>
      <div className="d-flex justify-content-between align-items-center mb-3">
        <div>
          <span className="badge bg-primary">Total Participants: {leaderboard.length}</span>
        </div>
        <button className="btn btn-primary">
          <i className="bi bi-arrow-clockwise"></i> Refresh
        </button>
      </div>
      <div className="table-responsive">
        <table className="table table-hover">
          <thead>
            <tr>
              <th>Rank</th>
              <th>User</th>
              <th>Total Points</th>
              <th>Total Activities</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.length > 0 ? (
              leaderboard.map((entry, index) => (
                <tr key={entry.id} className={index < 3 ? 'table-warning' : ''}>
                  <td>{getRankBadge(index + 1)}</td>
                  <td><strong>{entry.user}</strong></td>
                  <td>
                    <span className="badge bg-primary">{entry.total_points} pts</span>
                  </td>
                  <td>
                    <span className="badge bg-info">{entry.total_activities} activities</span>
                  </td>
                  <td>
                    <button className="btn btn-sm btn-outline-primary">View Profile</button>
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="5" className="text-center text-muted">
                  <div className="py-4">
                    <p className="mb-0">No leaderboard data found</p>
                  </div>
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Leaderboard;
