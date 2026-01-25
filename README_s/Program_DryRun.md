# 🔍 Simple Dry Run:

> ## Initialise
> ```
>   Word: banana 
>   Attempts: 6
>   Guessed letters: { }
>   Display: _ _ _ _ _ _
> ```


> ## Turn 1
>```
> Input: a
> Valid letter
> Correct guess
>```
>```
> Display: _ a _ a _ a
> Attempts: 6
> Guessed: {a}
> ```

> ## Turn 2
>```
> Input: z
> Valid letter
> Wrong guess
>```
>```
> Display: _ a _ a _ a
> Attempts: 5
> Guessed: {a, z}
>```

> ## Turn 3
>```
> Input: a
> Already guessed
>```
>```
> Message: Already guessed
> Attempts: 5
>```

> ## Turn 4
>```
> Input: 1
> Invalid input
>```
>```
> Message: Invalid input
> Attempts: 5
>```

> ## Turn 5
>```
> Input: b
> Correct guess
>```
>```
> Display: b a _ a _ a
> Attempts: 5
>```

> ## Turn 6
>```
> Input: n
> Correct guess
>```
>```
> Display: b a n a n a
>```

> ## ✅ Result
>```
> All letters guessed
> Player wins
>```
>```
> Output:
> You won! Word = banana
> Attempts left: 5
>```