import java.util.Scanner;
import java.util.concurrent.*;
public class multhe{
public static void main(String[] args) throws InterruptedException, ExecutionException {
try (Scanner sc= new Scanner(System.in)) {
System.out.print("String: ");
String st= sc.nextLine();
ExecutorService ex= Executors.newSingleThreadExecutor(); 
Future<String> future = ex.submit(() -> rev(st));
String rev= future.get();
System.out.println("String after Reversal : " + rev);
ex.shutdown();}}
private static String rev(String srt) {
if (srt.length() <= 1) {
return srt;} else {
char primary= srt.charAt(0);
char secondry= srt.charAt(srt.length() - 1);
String center= srt.substring(1, srt.length() - 1);
return secondry+ rev(center) +primary;
}
}
}