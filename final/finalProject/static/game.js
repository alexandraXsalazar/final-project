document.addEventListener('DOMContentLoaded', function () {
    const gameArea = document.getElementById('game');
    const duck = document.getElementById('duck');
    const scoreDisplay = document.getElementById('score');
    let score = 0;

    // Function to generate bugs
    function generateBug() {
        const bug = document.createElement('div');
        bug.className = 'bug';
        bug.style.left = Math.random() * (gameArea.offsetWidth - 20) + 'px';
        gameArea.appendChild(bug);

        // Animation to make bugs fall
        const bugFall = setInterval(function () {
            const duckTop = duck.offsetTop;
            const duckBottom = duck.offsetTop + duck.offsetHeight;
            const bugTop = bug.offsetTop + bug.offsetHeight;
            const bugLeft = bug.offsetLeft;
            const bugRight = bug.offsetLeft + bug.offsetWidth;

            if (bugTop >= gameArea.offsetHeight) {
                clearInterval(bugFall);
                bug.remove();
            } else if (duckBottom >= bugTop && duckTop <= bugTop && duckLeft < bugRight && duckRight > bugLeft) {
                clearInterval(bugFall);
                bug.remove();
                score++;
                scoreDisplay.textContent = 'Score: ' + score;
            } else {
                bug.style.top = bug.offsetTop + 2 + 'px';
            }
        }, 20);
    }

    // Move duck with arrow keys
    document.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowLeft') {
            moveDuck(-20);
        } else if (e.key === 'ArrowRight') {
            moveDuck(20);
        }
    });

    function moveDuck(distance) {
        const newLeft = duck.offsetLeft + distance;
        if (newLeft >= 0 && newLeft <= gameArea.offsetWidth - duck.offsetWidth) {
            duck.style.left = newLeft + 'px';
        }
    }

    // Generate bugs every 2 seconds
    setInterval(generateBug, 2000);
});
