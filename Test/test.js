var typed = new Typed(".auto-type", {
    strings: ["Loading ....."],
    typeSpeed: 55,
    backSpeed: 55,
    backDelay: 1000,
    loop:true
})

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry)
        if (entry.isIntersecting) {
            entry.target.classList.add('show');
        }
        else {
            entry.target.classList.remove('show');
        }
    });
});

const hiddenelements1 = document.querySelectorAll('.hidden');
hiddenelements1.forEach((el) => observer.observe(el));