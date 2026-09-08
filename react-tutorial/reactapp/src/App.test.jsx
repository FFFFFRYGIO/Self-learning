import { render, screen } from '@testing-library/react';
import App from './App';

test('renders the todo app', () => {
  render(<App />);
  const heading = screen.getByText(/todo app/i);
  expect(heading).toBeInTheDocument();
});
