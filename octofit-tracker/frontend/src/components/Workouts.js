import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

  useEffect(() => {
    console.log('Workouts component - Fetching from:', apiUrl);
    
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts component - Raw data received:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        console.log('Workouts component - Processed data:', workoutsData);
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Workouts component - Error fetching data:', error);
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

  return (
    <div className="container mt-4">
      <div className="page-header text-center">
        <h2>Workout Suggestions</h2>
        <p className="mb-0 mt-2">Explore superhero-inspired workout programs</p>
      </div>
      <div className="d-flex justify-content-between align-items-center mb-3">
        <div>
          <span className="badge bg-primary">Total Workouts: {workouts.length}</span>
        </div>
        <button className="btn btn-primary">
          <i className="bi bi-plus-circle"></i> Create Workout
        </button>
      </div>
      <div className="table-responsive">
        <table className="table table-hover">
          <thead>
            <tr>
              <th>Workout Name</th>
              <th>Category</th>
              <th>Difficulty</th>
              <th>Duration (min)</th>
              <th>Description</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {workouts.length > 0 ? (
              workouts.map(workout => (
                <tr key={workout.id}>
                  <td><strong>{workout.name}</strong></td>
                  <td>
                    <span className="badge bg-success">{workout.category}</span>
                  </td>
                  <td>
                    <span className={`badge ${
                      workout.difficulty === 'beginner' ? 'bg-info' :
                      workout.difficulty === 'intermediate' ? 'bg-warning' :
                      'bg-danger'
                    }`}>
                      {workout.difficulty ? workout.difficulty.charAt(0).toUpperCase() + workout.difficulty.slice(1) : 'N/A'}
                    </span>
                  </td>
                  <td>{workout.duration}</td>
                  <td>{workout.description}</td>
                  <td>
                    <button className="btn btn-sm btn-outline-success me-2">Start</button>
                    <button className="btn btn-sm btn-outline-primary">Details</button>
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="6" className="text-center text-muted">
                  <div className="py-4">
                    <p className="mb-0">No workouts found</p>
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

export default Workouts;
