<template>
<div>
  <Navbar Home='True' />
  <main class="main-content">
				<div class="container">
					<div class="page">
						<div class="row">
							<div class="col-md-9">
								<div class="slider">
									<ul class="slides">
                    <!-- Slide -->
										<li style="width: 100%; float: left; margin-right: -100%; position: relative; opacity: 1; display: block; z-index: 2;" class="flex-active-slide"><a href="#"><img src="dummy/slide-1.jpg" alt="Slide 1" draggable="false"></a></li>
                  </ul>
								<ul class="flex-direction-nav"><li><a class="flex-prev" href="#"><i class="fa fa-chevron-left"></i></a></li><li><a class="flex-next" href="#"><i class="fa fa-chevron-right"></i></a></li></ul></div>
							</div>
							<div class="col-md-3">
								<div class="row">
									<div class="col-sm-6 col-md-12">
                    <!-- left-thumb 2-->
										<div class="latest-movie">
											<a href="#"><img src="dummy/thumb-1.jpg" alt="Movie 1"></a>
										</div>
									</div>
								</div>
							</div>
						</div> <!-- .row -->
						<div class="row">
              <!-- down thumb 4 -->
							<div class="col-sm-6 col-md-3">
								<div class="latest-movie">
									<a href="#"><img src="dummy/thumb-3.jpg" alt="Movie 3"></a>
								</div>
							</div>
						</div> <!-- .row -->
						
						<div class="row">
							<div class="col-md-4">
								<h2 class="section-title">December premiere</h2>
								<p>Lorem ipsum dolor sit amet consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.</p>
								<ul class="movie-schedule">
									<li>
										<div class="date">16/12</div>
										<h2 class="entry-title"><a href="#">Perspiciatis unde omnis</a></h2>
									</li>
									<li>
										<div class="date">16/12</div>
										<h2 class="entry-title"><a href="#">Perspiciatis unde omnis</a></h2>
									</li>
									<li>
										<div class="date">16/12</div>
										<h2 class="entry-title"><a href="#">Perspiciatis unde omnis</a></h2>
									</li>
									<li>
										<div class="date">16/12</div>
										<h2 class="entry-title"><a href="#">Perspiciatis unde omnis</a></h2>
									</li>
								</ul> <!-- .movie-schedule -->
							</div>
							<div class="col-md-4">
								<h2 class="section-title">November premiere</h2>
								<p>Lorem ipsum dolor sit amet consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.</p>
								<ul class="movie-schedule">
									<li>
										<div class="date">16/12</div>
										<h2 class="entry-title"><a href="#">Perspiciatis unde omnis</a></h2>
									</li>
									<li>
										<div class="date">16/12</div>
										<h2 class="entry-title"><a href="#">Perspiciatis unde omnis</a></h2>
									</li>
									<li>
										<div class="date">16/12</div>
										<h2 class="entry-title"><a href="#">Perspiciatis unde omnis</a></h2>
									</li>
									<li>
										<div class="date">16/12</div>
										<h2 class="entry-title"><a href="#">Perspiciatis unde omnis</a></h2>
									</li>
								</ul> <!-- .movie-schedule -->
							</div>
							<div class="col-md-4">
								<h2 class="section-title">October premiere</h2>
								<p>Lorem ipsum dolor sit amet consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.</p>
								<ul class="movie-schedule">
									<li>
										<div class="date">16/12</div>
										<h2 class="entry-title"><a href="#">Perspiciatis unde omnis</a></h2>
									</li>
									<li>
										<div class="date">16/12</div>
										<h2 class="entry-title"><a href="#">Perspiciatis unde omnis</a></h2>
									</li>
									<li>
										<div class="date">16/12</div>
										<h2 class="entry-title"><a href="#">Perspiciatis unde omnis</a></h2>
									</li>
									<li>
										<div class="date">16/12</div>
										<h2 class="entry-title"><a href="#">Perspiciatis unde omnis</a></h2>
									</li>
								</ul> <!-- .movie-schedule -->
							</div>
						</div>
					</div>
				</div> <!-- .container -->
			</main>
      <Footer />

</div>
</template>

<script>
import Footer from "@/components/Footer";
import Navbar from "@/components/Navbar";
export default {
  name: "Home",
  components: {
    Navbar,
    Footer
  },
};
</script>

<style scoped>
</style>