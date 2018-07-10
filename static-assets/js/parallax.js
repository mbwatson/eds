const headerBackground = document.querySelector('.header__background')
// const headerForeground = document.querySelector('.header__foreground')

const mediumScreenQuery = window.matchMedia('(min-width: 768px)')

parallax = () => {
    if (mediumScreenQuery.matches) {
        headerBackground.style.backgroundPositionY = `${window.scrollY * 0.5}px`
    }
}

window.addEventListener('scroll', parallax)
