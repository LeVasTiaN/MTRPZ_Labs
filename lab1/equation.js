const readline = require('readline');

function isNumeric(value) {
    return !isNaN(value) && isFinite(value);
}

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

function askForNumber(rl, promptText, allowZero = true) {
    return new Promise((resolve) => {
        const ask = () => {
            rl.question(promptText, (input) => {
                const value = parseFloat(input);
                if (!isNumeric(value) || (!allowZero && value === 0)) {
                    console.log(
                        !isNumeric(value)
                            ? `Invalid input. Expected a valid real number, got ${input} instead.`
                            : 'Invalid input. "a" cannot be 0 in a quadratic equation.'
                    );
                    ask();
                } else {
                    resolve(value);
                }
            });
        };
        ask();
    });
}

async function runInteractiveMode() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    const a = await askForNumber(rl, 'Enter a: ', false);
    const b = await askForNumber(rl, 'Enter b: ');
    const c = await askForNumber(rl, 'Enter c: ');

    solveQuadratic(a, b, c);
    rl.close();
}

const args = process.argv.slice(2);

if (args.length === 0) {
    runInteractiveMode();
} else {
    runNonInteractiveMode();
}
