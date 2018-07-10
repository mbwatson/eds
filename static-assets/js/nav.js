const header = document.querySelector('header')
const navBar = document.querySelector('nav')
const menu = document.querySelector('.nav__list')
const hamburger = document.querySelector('.hamburger')

const largeScreenQuery = window.matchMedia( "(min-width: 768px)" );

function placeNavbar() {
    if ((window.scrollY >= header.offsetHeight) && (largeScreenQuery.matches)) {
        document.body.style.paddingTop = `${navBar.offsetHeight}px`
        document.body.classList.add('navbar-fixed')
        document.body.classList.remove('navbar-out')
    } else {
        document.body.style.paddingTop = 0
        document.body.classList.remove('navbar-fixed')
    }
}

// Place navigation bar, depending on scrolled amount

window.addEventListener('load', placeNavbar)
window.addEventListener('scroll', placeNavbar)

// Toggle menu into/out of view

hamburger.addEventListener('click', () => {
    document.body.classList.toggle('navbar-out');
})