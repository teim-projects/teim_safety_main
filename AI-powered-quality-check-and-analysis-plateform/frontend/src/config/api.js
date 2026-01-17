// src/config/api.js

// Detect local vs production automatically
const isLocalhost =
  window.location.hostname === 'localhost' ||
  window.location.hostname === '127.0.0.1';

// API base URL
export const API_BASE_URL = isLocalhost
  ? 'http://127.0.0.1:8000'
  : '';

