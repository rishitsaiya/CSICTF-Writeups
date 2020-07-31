## The Climb
The main idea finding the flag is decrypting the Hill Cipher.

#### Step-1:
After I downloaded `theclimb.java` & `theclimb.txt`, I checked out the contents in them.

 - `theclimb.txt` had this:

```
Encrypted text = lrzlhhombgichae
```

- `theclimb.java` had this:

```java
public class Main
{
    int kmatrix[][];
    int tmatrix[];
    int rmatrix[];
 
    public void div(String temp, int size)
    {
        while (temp.length() > size)
        {
            String substr = temp.substring(0, size);
            temp = temp.substring(size, temp.length());
            perf(substr);
        }
        if (temp.length() == size)
            perf(temp);
        else if (temp.length() < size)
        {
            for (int i = temp.length(); i < size; i++)
                temp = temp + 'x';
            perf(temp);
        }
    }
 
    public void perf(String text)
    {
        textconv(text);
        multiply(text.length());
        res(text.length());
    }
 
    public void keyconv(String key, int len)
    {
        kmatrix = new int[len][len];
        int c = 0;
        for (int i = 0; i < len; i++)
        {
            for (int j = 0; j < len; j++)
            {
                kmatrix[i][j] = ((int) key.charAt(c)) - 97;
                c++;
            }
        }
    }
 
    public void textconv(String text)
    {
        tmatrix = new int[text.length()];
        for (int i = 0; i < text.length(); i++)
        {
            tmatrix[i] = ((int) text.charAt(i)) - 97;
        }
    }
 
    public void multiply(int len)
    {
        rmatrix = new int[len];
        for (int i = 0; i < len; i++)
        {
            for (int j = 0; j < len; j++)
            {
                rmatrix[i] += kmatrix[i][j] * tmatrix[j];
            }
            rmatrix[i] %= 26;
        }
    }
 
    public void res(int len)
    {
        String res = "";
        for (int i = 0; i < len; i++)
        {
            res += (char) (rmatrix[i] + 97);
        }
        System.out.print(res);
    }
 
 
    public static void main(String[] args)
    {
        Main obj = new Main();
        System.out.println("Enter the plain text: ");
        String text = "fakeflag";
        System.out.println(text);
        System.out.println("Enter the key: ");
        String key = "gybnqkurp";
        System.out.println(key);
        double root = Math.sqrt(key.length());
        if (root != (long) root)
            System.out.println("Invalid key length.");
        else
        {
            int size = (int) root;
               
                System.out.println("Encrypted text = ");
                obj.keyconv(key, size);
                obj.div(text, size);
        }
    }
}
```

#### Step-2:
The flag is encrypted using [Hill cipher](https://en.wikipedia.org/wiki/Hill_cipher), in which every block of 3 is multiplied by a 3x3 matrix.

The official way to solve it is by solving a system of equations using [Gaussian elimination](https://en.wikipedia.org/wiki/Gaussian_elimination) but I prefer Bruteforcing all triagram combinations.

#### Step-3:
So, I wrote `Main.java` to get the flag.

```java
public class ClimbSolver {
    static String encrypted = "lrzlhhombgichae";
    static String key = "gybnqkurp";
    
    public static void brute(int startPos) {
        int size = (int) Math.sqrt(key.length());
        String encChunk = encrypted.substring(startPos, startPos + size);
        Main obj = new Main();
        obj.keyconv(key, size);
        for (char a = 'a'; a <= 'z'; a++)
        for (char b = 'a'; b <= 'z'; b++)
        for (char c = 'a'; c <= 'z'; c++) {
            String text = "" + a + b + c;
            obj.textconv(text);
            obj.multiply(text.length());
            String res = obj.res(text.length());
            if (res.equals(encChunk)) {
                System.out.print(text);
            }
        }
    }
    
    public static void main(String[] args) {
        for (int i = 0; i < encrypted.length(); i += 3) {
            brute(i);
        }
        System.out.println();
    }
}
```
After running the script, I got the flag.

#### Step-4:
Finally the flag becomes:
`csictf{hillshaveeyes}`