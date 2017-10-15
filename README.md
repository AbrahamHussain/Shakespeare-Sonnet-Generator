# Shakespeare-Sonnet-Generator

The goal of this project was to create a sonnet using a hidden markov model that is trained on Shakespeare's 154 sonnets. There were a lot of parameters that we had to take in, especially during the preprocessing. The bulk of our work was deciding on how we wanted to break up the sonnets to train the model (which will be talked about more in the tokenization section). Other parameters that we had to decided on were how we many states and iterations would give us the beset results (generate the most reasonable sounding poem).

Tokenization
The tokenization was one of the more time consuming parts of this project. Our first approach was to break down the sonnets into quatrains such that we would generate a quatrain at a time, but we later decided that if we did do it this way, we would not have a large enough data set. The next approach was to break the sonnets down into lines but we decided to move further down into tokenizing the poems into words for the same reasons as why we moved from quatrains to lines. We first tokenized the sonnets by splitting each line of each sonnet into its constituent words. Words that had punctuation associated with them (commas, periods, parenthesis etc.) were left the way they were in the sonnets initially but we decided to strip the sonnets of their punctuation because our first couple of generated poems had plenty of grammar mistakes due to misused punctuation. We also decided to add $\%$ characters to each line to add the number of element in every line up to ten. This was to ensure that our inputs would be constant in size each time. After tokenizing our sonnets in this manner, we printed them into a new .txt file line by line, using a - symbol to separate inputs of lines.

Algorithm
We primarily utilized the homework 5 to implement the Baum-Welch Algorithm, tokenizing our data in a manner that matched the ron.txt file so we did not have to play around with the solutions as much. Perhaps the most vital decision was our selection of states and iterations to generate an emission that sounded/looked the most like a sonnet. We started first with 4 hidden states and 10 iterations and immediately noticed a troubling trend: our poems had repeated words. We first, incorrectly, believed this could be fixed by increasing the number of iterations we used so we tried 20-40 iterations but this still generated poems with repeating words. We then realized that this issued lied not in the number of iterations but on the number of hidden states we trained our HMM on. So we moved to 10 hidden states and 10 iterations, noticing a significant improvement in our sonnet (only one to two repeating words and better syntax). As we still saw repeating words, we moved up to 20 hidden states and found now that no words were repeated in our sonnet and it actually began to resemble an attempt at human writing. Given this trend in increasing number of hidden states and more accurate poem generation, we decided to generate our final poem at 50 hidden states and 10 iterations.

Poetry Generation
Our first step was to just generate something that resembled a poem, an emission with 14 lines and 10 words per line. We accomplished this by editing the generate emissions portion the homework 5 solutions to generate 14 different emissions instead of just 1 and setting our desired output length to be 10.

Once we got this part to work, it was time for the optimization. The first thing that we decided to do was make sure that every line is 10 syllables. We did this by first generating 10 words for every line like we did for our initial output. Once we did this, we used the NLTK package to count the syllables of every line and if we found a line that had more than 10 syllables we would do the following: we will first keep all the words up to 10 syllables and if one of the words exceeds that the 10 syllable limit then we will remove it. Now we are left with a line that may have less than 10 syllables if we happen to remove a word that exceeded 10 syllables. In order to fill the rest of the syllables, we are going to generated single words that are less than or equal to the syllable count that we must fill. We keep repeating this process until we end up with only 10 syllables per line. 
 
The second improvement that we did was to create a rhyming pattern. We developed a Shakespearean sonnet which would follow the rhyme scheme ABABCDCDEFEFGG. In order to make this process simpler, we created quatrains individually by making sure that the last word rhymed with the line 2 above it so that it follows an ABAB pattern. We did this 3 times to create the 3 quatrains and then created a 2 line couplet in a similar manner except both of the lines were made to rhyme. We used an open source package called Poetry-tool to find words that rhyme and generated last words until they did rhyme.

As we added more hidden states to our model, we noticed that our generated poems began to attain greater amounts of structure. What we mean by structure primarily revolves around the fact that generated lines began to follow or attempt to follow general rules of English speech. Verbs typically did not follow verbs but rather would follow nouns. Furthermore, adjectives preceded more nouns than they did verbs. These slight improvements made the sonnets sound more 'real'. Additionally, most of our sonnets followed a general theme about love, relationships, and nature, presumably because this is what Shakespeare wrote about the most and as such, words related to these subjects would appear greater in frequency in his corpus. Of course, what did not make sense from the very beginning and even to the end was overall syntax. The generated poems, while following syntax in parts, did not follow correct English form throughout the entirety of the sonnet. This may be because we generated our emissions line by line (and quatrains by quatrains) vs an entire sonnet at a time.


Conclusion
The generated sonnets definitely left much to be desired. A perfect model would have generated sonnets with an accurate rhyming scheme, number of syllables, iambic pentameter, and sentence structure. However, the way we tokenized our data and applied our model did not lead to this naturally. Rather, we had to forcefully constrain our generated lines to be below ten lines in length and have an ending rhyme.