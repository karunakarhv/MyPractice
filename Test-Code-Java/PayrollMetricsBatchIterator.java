import java.util.Collection;
import java.util.Iterator;
import java.util.NoSuchElementException;

public class PayrollMetricsBatchIterator<T> implements Iterator<Collection<T>> {

    private final int batchCount;
    private final Iterator<T> items;
    private final int count;
    private int offset = 0;

    public PayrollMetricsBatchIterator(int batchCount, Collection<T> items) {
        if (batchCount <= 0) {
        throw new RuntimeException("The batch count should be more then 0");
        }
        this.batchCount = batchCount;
        this.items = items.iterator();
        this.count = items.size();
    }
}