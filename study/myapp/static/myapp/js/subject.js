// document.addEventListener('DOMContentLoaded', function() {
//     const wordBlocks = document.querySelectorAll('.word-block');
//     const alphabetLetters = document.querySelectorAll('.alphabet-letter');

//     alphabetLetters.forEach(letter => {
//         letter.addEventListener('click', function() {
//             const letterClicked = this.innerText;
//             wordBlocks.forEach(block => {
//                 const firstLetter = block.querySelector('.word-topic').innerText.trim().charAt(0).toUpperCase();
//                 if (firstLetter === letterClicked) {
//                     block.classList.remove('hide');
//                 } else {
//                     block.classList.add('hide');
//                 }
//             });
//         });
//     });
// });