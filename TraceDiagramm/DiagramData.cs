using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using Microsoft.Extensions.Configuration;

namespace TraceDiagramm
{
    public class DiagramData
    {
        public List<DCCategory> Categories { get; set; }
    }

    public class DCCategory
    {
        public string Label { get; set; }
        public List<DCPair>Data { get; set; }
    }

    public class DCPair
    {
        public DateTime X { get; set; }
        public int Y { get; set; }
    }


}