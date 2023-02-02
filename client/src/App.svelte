<script>
	import {onMount} from 'svelte';
	import PopularMovies from "./components/PopularMovies.svelte";
	// import SearchMovies from "../components/SearchMovies.svelte";
	import {fly} from 'svelte/transition';
	let popular_movies=[];
	let loaded=false;
	onMount(async() => {
		const movies_res = await fetch('./popular_movies');
		const movies_json  = await movies_res.json(); 	
		popular_movies = movies_json.results;
		loaded=true;
	});

	console.log(loaded);

</script>

<section in:fly={{y:50, duration:500, delay:500}} out:fly={{duration:500}}>
	
    <!-- <SearchMovies /> -->
    <PopularMovies movies={popular_movies}/> 
</section> 
