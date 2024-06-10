const player = document.getElementById('player');
const scoreDisplay = document.getElementById('score');
let score = 0;

const gameArea = document.getElementById('game-area');
const gameAreaWidth = gameArea.clientWidth;
const gameAreaHeight = gameArea.clientHeight;
const playerSpeed = 10;
let fallingSpeed = 2;

document.addEventListener('keydown', (event) => {
    let playerLeft = parseInt(window.getComputedStyle(player).getPropertyValue('left'));
    if (event.key === 'ArrowLeft' && playerLeft > 0) {
        player.style.left = playerLeft - playerSpeed + 'px';
    } else if (event.key === 'ArrowRight' && playerLeft < gameAreaWidth - player.clientWidth) {
        player.style.left = playerLeft + playerSpeed + 'px';
    }
});

function startFalling() {
    const fallingObject = document.createElement('div');
    fallingObject.className = 'falling-object';
    fallingObject.style.top = '0px';
    fallingObject.style.left = Math.floor(Math.random() * (gameAreaWidth - fallingObject.clientWidth)) + 'px';
    gameArea.appendChild(fallingObject);
    fall(fallingObject);
}

function fall(fallingObject) {
    let fallingObjectTop = parseInt(window.getComputedStyle(fallingObject).getPropertyValue('top'));
    if (fallingObjectTop < gameAreaHeight) {
        fallingObject.style.top = fallingObjectTop + fallingSpeed + 'px';
        requestAnimationFrame(() => fall(fallingObject));
        if (checkCollision(player, fallingObject)) {
            score += 1;
            scoreDisplay.textContent = 'Puntos: ' + score;
            resetFallingObject(fallingObject);
        }
    } else {
        resetFallingObject(fallingObject);
    }
}

function checkCollision(div1, div2) {
    const rect1 = div1.getBoundingClientRect();
    const rect2 = div2.getBoundingClientRect();

    return !(rect1.right < rect2.left ||
             rect1.left > rect2.right ||
             rect1.bottom < rect2.top ||
             rect1.top > rect2.bottom);
}

function resetFallingObject(fallingObject) {
    fallingObject.style.top = '0px';
    fallingObject.style.left = Math.floor(Math.random() * (gameAreaWidth - fallingObject.clientWidth)) + 'px';
}

setInterval(startFalling, 2000);
