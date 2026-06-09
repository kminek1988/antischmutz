gsap.registerPlugin(ScrollTrigger, ScrollSmoother);
// fade-left animation

  gsap.utils.toArray(".fade-left").forEach((element) => {
    gsap.fromTo(element,
      {
        opacity: 0,
        x: -80
      },
      {
        opacity: 1,
        x: 0,
        duration: 1,
        ease: "power3.out",
        scrollTrigger: {
          trigger: element,
          start: "top 80%",
          toggleActions: "play none none reverse"
        }
      }
    );
  });
// fade-right animation

  gsap.utils.toArray(".fade-right").forEach((element) => {
    gsap.fromTo(element,
      {
        opacity: 0,
        x: 80
      },
      {
        opacity: 1,
        x: 0,
        duration: 1,
        ease: "power3.out",
        scrollTrigger: {
          trigger: element,
          start: "top 80%",
          toggleActions: "play none none reverse"
        }
      }
    );
  });
//   fade-in
 gsap.utils.toArray(".fade-in").forEach((element) => {
    gsap.fromTo(element,
      {
        opacity: 0,
        y: -80
      },
      {
        opacity: 1,
        y: 0,
        duration: 1,
        ease: "power3.out",
        scrollTrigger: {
          trigger: element,
          start: "top 80%",
          toggleActions: "play none none reverse"
        }
      }
    );
  });

// create the scrollSmoother before your scrollTriggers
ScrollSmoother.create({
	smooth: 1, // how long (in seconds) it takes to "catch up" to the native scroll position
	effects: true, // looks for data-speed and data-lag attributes on elements
	smoothTouch: 0.1 // much shorter smoothing time on touch devices (default is NO smoothing on touch devices)
});