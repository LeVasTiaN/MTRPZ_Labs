const readline = require('readline');
function solveQuadratic(a, b, c) {
    console.log(`Equation is: ${a}x^2 + ${b}x + ${c} = 0\n`)
    const discriminant = b * b - 4 * a * c;
    if (discriminant > 0) {
        const root1 = (-b + Math.sqrt(discriminant)) / (2 * a);
        const root2 = (-b - Math.sqrt(discriminant)) / (2 * a);
        console.log(`There are two roots: x1 = ${root1}, x2 = ${root2}`);
    } else if (discriminant === 0) {
        const root = -b / (2 * a);
        console.log(`There is one root: x = ${root}`);
    } else {
        console.log('No real roots exist.');
    }
}
function runInteractiveMode() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question('Enter a: ', (a) => {
        rl.question('Enter b: ', (b) => {
            rl.question('Enter c: ', (c) => {
                solveQuadratic(a, b, c);
                rl.close();
            });
        });
    });
}

const args = process.argv.slice(2)

if (args.length === 0) {
    runInteractiveMode();
} else {
    runNonInteractiveMode();
}
