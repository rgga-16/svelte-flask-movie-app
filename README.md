How to run this app:
1) To run, open 2 terminals.
2) In terminal 1, run "cd client", then "npm install", then "npm run dev".
3) In terminal 2, run "python app.py".

How to create this kind of Svelte+Flask template
1) Create app.py. Import flask there.
2) To create the client-side of the app using Svelte, run "npx degit sveltejs/template client"
3) Run "cd client" and then, "npm install".

Note to self: Svelte by itself can only be used with Flask. Flask doesn't work well with Sveltekit.
