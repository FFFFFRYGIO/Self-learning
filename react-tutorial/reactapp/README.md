# React Todo app

A small todo app built while learning React.

It was originally bootstrapped with [Create React App](https://github.com/facebook/create-react-app)
and later moved to [Vite](https://vite.dev/). Create React App was deprecated in
2025 and its last release (`react-scripts` 5.0.1) still pulls in an unpatched
`webpack-dev-server`, so the build tooling was swapped out. The React code itself
is unchanged.

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in development mode with hot module replacement.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

`npm run dev` does the same thing — it is the name Vite uses by convention.

### `npm test`

Runs the tests once with [Vitest](https://vitest.dev/) and exits.\
Use `npm run test:watch` for the interactive watch mode.

### `npm run build`

Builds the app for production to the `build` folder.\
The build is minified and the filenames include hashes.

### `npm run preview`

Serves the contents of `build` locally, so you can check the production bundle
before deploying it.

## Notes on the project layout

Vite expects a couple of things in different places than Create React App did:

- `index.html` lives in the project root, not in `public/`, and it loads
  `src/index.jsx` directly with a `<script type="module">` tag.
- `%PUBLIC_URL%` no longer exists. Files in `public/` are served from `/`, so
  the favicon is just `/favicon.ico`.
- Files containing JSX use the `.jsx` extension.
- Configuration lives in `vite.config.js`, including the Vitest setup.
