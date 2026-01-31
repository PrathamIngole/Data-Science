*STACK* --

        -- stack is a linear data structure.
        -- it is a contineous memory allocation for objects.
        -- Follows Last - In - First - Out (LIFO).
        --  Insert : O1, O2, O3, O4, O5

                        |             |
                        |      o5     |
                        |      O4     |
                        |      O3     |
                        |      O2     |
                        |      O1     |
                        |_____________|


        -- Out : O5 --> O4 --> O3 --> O2 --> O1

        -- Operation can be performed on stack :
                                    
                                1. push --> inserting an element.
                                2. pop --> removing last element.
                                3. peep --> returning last element from the stack.
                                4. size --> Number of elements in stack.
                                5. isEmpty -> true if stack is empty otherwise False.
                                6. display -> printing the elements of the stack.

        -- Implimentation Of stack :

                                1. Container -> which stores the elements.
                                2. top -> points to the top most insertion.

                    -- when a object/element is inserted then the top is incremented.
                    -- when a object/element is deleted then the top is decremented.
                
                1. using List/array 
                2. collection.deque
                3. using our own implimentation

                